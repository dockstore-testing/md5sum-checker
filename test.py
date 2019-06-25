import subprocess
import unittest


class TestMd5sumChecker(unittest.TestCase):
    # For each workflow, verify that it succeeds when the input file's md5sum matches and fails when it does not
    def test_cwl_success(self):
        process = subprocess.call(["cwltool", "checker-workflow-wrapping-tool.cwl", "checker-input-cwl.json"])
        self.assertEqual(process, 0)

    def test_cwl_failure(self):
        process = subprocess.call(["cwltool", "checker-workflow-wrapping-tool.cwl", "checker-fail-cwl.json"])
        self.assertEqual(process, 1)

    def test_wdl_success(self):
        process = subprocess.call(["java", "-jar", "cromwell-42.jar", "run", "checker-workflow-wrapping-workflow.wdl",
                                  "-i", "md5sum-wdl.json"])
        self.assertEqual(process, 0)

    def test_wdl_failure(self):
        process = subprocess.call(["java", "-jar", "cromwell-42.jar", "run", "checker-workflow-wrapping-workflow.wdl",
                                  "-i", "md5sum-fail-wdl.json"])
        self.assertEqual(process, 1)


if __name__ == '__main__':
    unittest.main()
