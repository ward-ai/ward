"""
Tests for the main module.
"""

from aia.__main__ import main

def test_main(capsys):
    """Test the main function."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Welcome to AIA!\n" 