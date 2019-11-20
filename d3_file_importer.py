import tarfile
import wget

print("Beginning file download")

url = "https://s3.amazonaws.com/aot-tarballs/chicago-complete.monthly.2018-10-01-to-2018-10-31.tar"

file_dest = "/mnt/orangefs/AoT_Chicago.oct.tar"

wget.download(url, file_dest)

print("File download complete. Starting Tar extraction")

tf = tarfile.open(file_dest)

tf.extractall("/mnt/orangefs")
