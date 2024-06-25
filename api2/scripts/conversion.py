import aspose.threed as a3d
import os
UPLOAD_FOLDER = '/var/www/api/uploads'
DOWNLOAD_FOLDER = '/var/www/api/downloads'

filename = os.path.join(UPLOAD_FOLDER, 'Room.usdz')
downloadname = os.path.join(DOWNLOAD_FOLDER, 'output.xyz')
os.system('usd2gltf -i ' + filename + ' -o /var/www/api/scripts/Room.glb')
scene = a3d.Scene.from_file("/var/www/api/scripts/Room.glb")
scene.save(downloadname)
