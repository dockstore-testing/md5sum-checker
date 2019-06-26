task checkerTask {
  File inputFile
  String expectedMd5sum

  command {
    /bin/check_md5sum --input-file ${inputFile} --md5 ${expectedMd5sum}
  }

  runtime {
    docker: "quay.io/dockstore-testing/md5sum-checker:1.0.0"
  }
}
