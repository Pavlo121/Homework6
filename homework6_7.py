class FileProcessor:
    @staticmethod
    def write_to_file(file_path: str, data: str):
        with open(file_path, 'w') as file:
            file.write(data)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        with open(file_path, 'r') as file:
            return file.read()


import pytest
import os

def test_file_write_read(tmpdir):
    file = tmpdir.join("testfile.txt")
    FileProcessor.write_to_file(file, "Hello, World!")
    content = FileProcessor.read_from_file(file)
    assert content == "Hello, World!"

def test_file_write_large_data(tmpdir):
    file = tmpdir.join("largefile.txt")
    large_data = "A" * 10**6  # 1 MB of data
    FileProcessor.write_to_file(file, large_data)
    content = FileProcessor.read_from_file(file)
    assert content == large_data

def test_file_write_empty_string(tmpdir):
    file = tmpdir.join("emptyfile.txt")
    FileProcessor.write_to_file(file, "")
    content = FileProcessor.read_from_file(file)
    assert content == ""

def test_file_read_non_existent_file():
    with pytest.raises(FileNotFoundError):
        FileProcessor.read_from_file("non_existent_file.txt")

# Запуск pytest з тестами
if __name__ == '__main__':
    pytest.main()
