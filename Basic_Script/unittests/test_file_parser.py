import unittest
import shutil
from pathlib import Path
from Basic_Script.file_parser import scanning, JPEG_IMAGES, PNG_IMAGES, JPG_IMAGES, SVG_IMAGES, AVI_VIDEO, MP4_VIDEO, \
    MOV_VIDEO, \
    MKV_VIDEO, DOC_DOCUMENTS, DOCX_DOCUMENTS, TXT_DOCUMENTS, PDF_DOCUMENTS, XLSX_DOCUMENTS, PPTX_DOCUMENTS, MP3_MUSIC, \
    OGG_MUSIC, WAV_MUSIC, AMR_MUSIC, ZIP_ARCHIVE, GZ_ARCHIVE, TAR_ARCHIVE, MY_OTHERS, FOLDERS, EXTENSIONS, UNDEFINED


class TestFileParser(unittest.TestCase):
    def setUp(self):
        # Set up any necessary data or mock objects
        self.test_folder = Path(__file__).parent / "test_data"
        self.initialize_test_data()

    def initialize_test_data(self):
        # Create a temporary directory for test data
        test_data_dir = self.test_folder
        test_data_dir.mkdir(exist_ok=True)

        # Create test files in the temporary directory
        (test_data_dir / "image1.jpg").touch()
        (test_data_dir / "image2.png").touch()
        (test_data_dir / "image3.jpeg").touch()
        (test_data_dir / "image4.svg").touch()
        (test_data_dir / "video1.avi").touch()
        (test_data_dir / "video2.mp4").touch()
        (test_data_dir / "video3.mov").touch()
        (test_data_dir / "video4.mkv").touch()
        (test_data_dir / "document1.docx").touch()
        (test_data_dir / "document2.doc").touch()
        (test_data_dir / "document3.txt").touch()
        (test_data_dir / "document4.pdf").touch()
        (test_data_dir / "document5.xlsx").touch()
        (test_data_dir / "document6.pptx").touch()
        (test_data_dir / "music1.mp3").touch()
        (test_data_dir / "music2.ogg").touch()
        (test_data_dir / "music3.wav").touch()
        (test_data_dir / "music4.amr").touch()
        (test_data_dir / "archive1.zip").touch()
        (test_data_dir / "archive2.gz").touch()
        (test_data_dir / "archive3.tar").touch()
        (test_data_dir / "web.html").touch()
        (test_data_dir / "web.css").touch()
        

        # Create test folders in the temporary directory
        (test_data_dir / "subfolder1").mkdir(exist_ok=True)
        (test_data_dir / "subfolder2").mkdir(exist_ok=True)
        (test_data_dir / "subfolder3").mkdir(exist_ok=True)
        (test_data_dir / "subfolder4").mkdir(exist_ok=True)
        (test_data_dir / "subfolder5").mkdir(exist_ok=True)

        # Update self.test_folder to point to the temporary test data directory
        self.test_folder = test_data_dir

    def test_scanning(self):
        scanning(self.test_folder)

        # Add assertions to check if the files and folders have been correctly categorized
        self.assertGreater(len(JPEG_IMAGES), 0, "No JPEG images found.")
        self.assertGreater(len(PNG_IMAGES), 0, "No PNG images found.")
        self.assertGreater(len(JPG_IMAGES), 0, "No JPG images found.")
        self.assertGreater(len(SVG_IMAGES), 0, "No SVG images found.")
        self.assertGreater(len(AVI_VIDEO), 0, "No AVI videos found.")
        self.assertGreater(len(MP4_VIDEO), 0, "No MP4 videos found.")
        self.assertGreater(len(MOV_VIDEO), 0, "No MOV videos found.")
        self.assertGreater(len(MKV_VIDEO), 0, "No MKV videos found.")
        self.assertGreater(len(DOC_DOCUMENTS), 0, "No DOC documents found.")
        self.assertGreater(len(DOCX_DOCUMENTS), 0, "No DOCX documents found.")
        self.assertGreater(len(TXT_DOCUMENTS), 0, "No TXT documents found.")
        self.assertGreater(len(PDF_DOCUMENTS), 0, "No PDF documents found.")
        self.assertGreater(len(XLSX_DOCUMENTS), 0, "No XLSX documents found.")
        self.assertGreater(len(PPTX_DOCUMENTS), 0, "No PPTX documents found.")
        self.assertGreater(len(MP3_MUSIC), 0, "No MP3 music found.")
        self.assertGreater(len(OGG_MUSIC), 0, "No OGG music found.")
        self.assertGreater(len(WAV_MUSIC), 0, "No WAV music found.")
        self.assertGreater(len(AMR_MUSIC), 0, "No AMR music found.")
        self.assertGreater(len(ZIP_ARCHIVE), 0, "No ZIP archives found.")
        self.assertGreater(len(GZ_ARCHIVE), 0, "No GZ archives found.")
        self.assertGreater(len(TAR_ARCHIVE), 0, "No TAR archives found.")

        self.assertGreater(len(EXTENSIONS), 0, "No file types found.")
        self.assertGreater(len(UNDEFINED), 0, "No undefined file types found.")

        self.assertGreater(len(MY_OTHERS), 0, "No other files found.")
        self.assertGreater(len(FOLDERS), 0, "No folders found.")

    def tearDown(self):
        # Clean up any temporary test data created during the test
        shutil.rmtree(self.test_folder)


if __name__ == '__main__':
    unittest.main()
