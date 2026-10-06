"""Regression checks for client-project boundaries; uses synthetic temporary data."""
import tempfile
import unittest
from pathlib import Path
import shutil
import tomllib

from new_project import STUDIO, create_project


class ProjectBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp_parent = Path(tempfile.gettempdir()).resolve()
        self.root = Path(tempfile.mkdtemp(prefix='iguide-boundary-', dir=self.temp_parent)).resolve()

    def tearDown(self):
        # Verify the exact recursive-cleanup target belongs to this test's temp parent.
        assert self.root.parent == self.temp_parent
        assert self.root.name.startswith('iguide-boundary-')
        shutil.rmtree(self.root)

    def create(self, name):
        return create_project(self.root / name, name, 'Synthetische klant', 'Merkidentiteit')

    def test_separate_projects_and_instructions(self):
        a, b = self.create('project-a'), self.create('project-b')
        (a/'01-input/private.txt').write_text('Only A')
        self.assertFalse((b/'01-input/private.txt').exists())
        profiles = list((b/'.codex/agents').glob('*.toml'))
        self.assertEqual(len(profiles), 6)
        for profile in profiles:
            self.assertEqual(tomllib.loads(profile.read_text(encoding='utf-8'))['name'], profile.stem)
        self.assertTrue((b/'.opencode/skills/ui-ux-pro-max/scripts/search.py').is_file())
        self.assertTrue((b/'00-project/studio-baseline.json').is_file())

    def test_existing_directory_preserved(self):
        a = self.create('project-a')
        (a/'sentinel.txt').write_text('preserve')
        with self.assertRaises(FileExistsError): self.create('project-a')
        self.assertEqual((a/'sentinel.txt').read_text(), 'preserve')

    def test_nested_client_project_rejected(self):
        a = self.create('project-a')
        with self.assertRaises(ValueError):
            create_project(a/'nested'/'project-b', 'project-b', 'B', 'B')
        self.assertFalse((a/'nested').exists())

    def test_git_ancestor_rejected(self):
        repo = self.root/'checkout'
        repo.mkdir()
        (repo/'.git').write_text('gitdir: elsewhere')
        with self.assertRaises(ValueError):
            create_project(repo/'project', 'project', 'B', 'B')
        self.assertFalse((repo/'project').exists())

    def test_studio_and_invalid_id_rejected(self):
        with self.assertRaises(ValueError):
            create_project(STUDIO/'client', 'client', 'B', 'B')
        with self.assertRaises(ValueError):
            create_project(self.root/'invalid', '../invalid', 'B', 'B')
        self.assertFalse((self.root/'invalid').exists())


if __name__ == '__main__':
    unittest.main()
