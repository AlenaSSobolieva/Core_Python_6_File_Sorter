import unittest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch
from Basic_Script.main_script import handle_media, handle_other, handle_archive, handle_folder, main

class TestMain(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test data
        self.test_data_dir = Path(tempfile.mkdtemp())
        self.test_data_dir.mkdir(exist_ok=True)

        # Create some sample files in the temporary directory
        (self.test_data_dir / "image1.jpg").touch()
        (self.test_data_dir / "image2.png").touch()
        (self.test_data_dir / "image3.jpeg").touch()
        (self.test_data_dir / "image4.svg").touch()
        (self.test_data_dir / "video1.avi").touch()
        (self.test_data_dir / "video2.mp4").touch()
        (self.test_data_dir / "video3.mov").touch()
        (self.test_data_dir / "video4.mkv").touch()
        (self.test_data_dir / "document1.docx").touch()
        (self.test_data_dir / "document2.doc").touch()
        (self.test_data_dir / "document3.txt").touch()
        (self.test_data_dir / "document4.pdf").touch()
        (self.test_data_dir / "document5.xlsx").touch()
        (self.test_data_dir / "document6.pptx").touch()
        (self.test_data_dir / "music1.mp3").touch()
        (self.test_data_dir / "music2.ogg").touch()
        (self.test_data_dir / "music3.wav").touch()
        (self.test_data_dir / "music4.amr").touch()
        (self.test_data_dir / "archive1.zip").touch()
        (self.test_data_dir / "archive2.gz").touch()
        (self.test_data_dir / "archive3.tar").touch()
        (self.test_data_dir / "web.html").touch()
        (self.test_data_dir / "web.css").touch()

    def tearDown(self):
        # Clean up the temporary test data directory
        shutil.rmtree(self.test_data_dir)

    def test_handle_media(self):
        # Test handle_media function
        media_file_jpeg = self.test_data_dir / "test_image.jpeg"
        target_folder_jpeg = self.test_data_dir / "images" / "JPEG"
        handle_media(media_file_jpeg, target_folder_jpeg)
        self.assertFalse(media_file_jpeg.exists())
        self.assertTrue((target_folder_jpeg / "test_image.jpeg").exists())

    #     media_file_jpg = self.test_data_dir / "test_image.jpg"
    #     target_folder_jpg = self.test_data_dir / "images" / "JPG"
    #     handle_media(media_file_jpg, target_folder_jpg)
    #     self.assertFalse(media_file_jpg.exists())
    #     self.assertTrue((target_folder_jpg / "test_image.jpg").exists())


    # def test_handle_other(self):
    #     # Test handle_other function
    #     other_file = self.test_data_dir / "test_document.docx"
    #     target_folder = self.test_data_dir / "other files"
    #
    #     handle_other(other_file, target_folder)
    #
    #     # Check if the file has been moved to the target folder with the correct name
    #     self.assertFalse(other_file.exists())
    #     self.assertTrue((target_folder / "test_document.docx").exists())
    #
    # def test_handle_archive(self):
    #     # Test handle_archive function
    #     archive_file = self.test_data_dir / "test_archive.zip"
    #     target_folder = self.test_data_dir / "archives" / "ZIP"
    #
    #     handle_archive(archive_file, target_folder)
    #
    #     # Check if the archive has been unpacked to the target folder
    #     self.assertFalse(archive_file.exists())
    #     self.assertTrue((target_folder / "test_archive").is_dir())
    #     self.assertTrue((target_folder / "test_archive" / "test_image.jpg").exists())
    #
    # def test_handle_folder(self):
    #     # Test handle_folder function
    #     test_folder = self.test_data_dir / "test_folder"
    #     test_folder.mkdir()
    #
    #     handle_folder(test_folder)
    #
    #     # Check if the folder has been deleted
    #     self.assertFalse(test_folder.exists())
    #
    def test_main(self):
        # Test the main function (integration test)
        # Note: This test may require additional mocking and setup
        with patch("Basic_Script.main_script.parser.scanning"):
            main(self.test_data_dir)

        # Add assertions to check if the files have been correctly categorized
        # You can use assertions similar to those in the file_parser tests
        # Example: self.assertGreater(len(parser.JPEG_IMAGES), 0, "No JPEG images found.")
        pass

if __name__ == '__main__':
    unittest.main()
