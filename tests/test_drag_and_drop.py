from pages.drag_and_drop_page import DragAndDropPage
import pytest
import time

def test_drag_a_to_b(main_page):
    """Test dragging column a to column b"""
    main_page.open()
    dnd_page = main_page.open_drag_and_drop_page()
    time.sleep(5)
    dnd_page.drag_source_to_target(dnd_page.column_a, dnd_page.column_b)
    assert "B" in dnd_page.column_a_header