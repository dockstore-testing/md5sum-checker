task md5 {
  File inputFile

  command {
    /bin/my_md5sum ${inputFile}
  }

 output {
    File value = "md5sum.txt"
 }

 runtime {
   docker: "quay.io/agduncan94/my-md5sum"
 }
}