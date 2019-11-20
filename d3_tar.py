import tarfile
import wget

file_dest = "/mnt/orangefs/AoT_Chicago.complete.latest.tar"

print("Starting Tar extraction")

tf = tarfile.open(file_dest)

tf.extractall("/mnt/orangefs")
