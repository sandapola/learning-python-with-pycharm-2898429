from unittest import TestCase
from cell import *


class TestCell(TestCase):
    def test_set_future_state(self):
        active_test_cell = Cell((0, 0), (0, 0), active=True)
        # neighbor count will have values from 0 to 8 inclusive.
        # This works because a cell can have 0 to 8 active neighbors

        # Active cells should only stay active if they have 2 or 3 neighbors
        for neighbor_count in range(9):
            active_test_cell.set_future_state(neighbor_count)
            if neighbor_count == 2 or neighbor_count == 3:
                self.assertTrue(active_test_cell.future_state, f'future_state should be true for {neighbor_count} neighbors')
            else:
                self.assertFalse(active_test_cell.future_state, f'future_state should be false for {neighbor_count} neighbors')

        # Inactive cells should only be activated if they have exactly 3 neighbors
        inactive_test_cell = Cell((0, 0), (0, 0), active=False)
        for neighbor_count in range(9):
            inactive_test_cell.set_future_state(neighbor_count)
            if neighbor_count == 3:
                self.assertTrue(inactive_test_cell.future_state, f'future_state should be true for {neighbor_count} neighbors')
            else:
                self.assertFalse(inactive_test_cell.future_state, f'future_state should be false for {neighbor_count} neighbors')

    def test_update(self):
        # scenario 1: inactive cell, which will become active
        inactive_cell = Cell((0, 0), (0, 0))
        self.assertFalse(inactive_cell.active)
        inactive_cell.future_state = True

        inactive_cell.update()
        self.assertTrue(inactive_cell.active, 'future_state was set to true so the cell should become active')
        self.assertIs(inactive_cell.future_state, None, 'future_state should be reset after an update')

        # scenario 2: active cell which will become inactive
        active_cell = Cell((0, 0), (0, 0), active=True)
        active_cell.future_state = False
        active_cell.update()
        self.assertFalse(active_cell.active, 'future_state was set to false so the cell should become inactive')
        self.assertIs(active_cell.future_state, None, 'future_state should be reset after an update')

    def test_flip(self):
        # test the flip method of the cell class
        cell = Cell((0, 0), (0, 0), active=True)
        self.assertTrue(cell.active)
        cell.flip()
        self.assertFalse(cell.active)
        cell.flip()
        self.assertTrue(cell.active)