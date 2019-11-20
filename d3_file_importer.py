import tarfile
import wget

print("Beginning file download")

url = "http://www.mcs.anl.gov/research/projects/waggle/downloads/datasets/AoT_Chicago.complete.latest.tar"

file_dest = "/mnt/orangefs/AoT_Chicago.complete.latest.tar"

wget.download(url, file_dest)

tf = tarfile.open("file_dest")

tf.extractall()
