import subprocess
import unittest


class TestMd5sumChecker(unittest.TestCase):
    def test_cwl_success(self):
        process = subprocess.run(["cwltool", "checker-workflow-wrapping-tool.cwl", "checker-input-cwl.json"])
        self.assertEqual(process.returncode, 0)

    def test_cwl_failure(self):
        process = subprocess.run(["cwltool", "checker-workflow-wrapping-tool.cwl", "checker-fail-cwl.json"])
        self.assertEqual(process.returncode, 1)

    def test_wdl_success(self):
        process = subprocess.run(["java", "-jar", "cromwell-42.jar", "run", "checker-workflow-wrapping-workflow.wdl",
                                  "-i", "md5sum-wdl.json"])
        self.assertEqual(process.returncode, 0)

    def test_wdl_failure(self):
        process = subprocess.run(["java", "-jar", "cromwell-42.jar", "run", "checker-workflow-wrapping-workflow.wdl",
                                  "-i", "md5sum-fail-wdl.json"])
        self.assertEqual(process.returncode, 1)


if __name__ == '__main__':
    unittest.main()
