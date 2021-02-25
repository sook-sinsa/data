import labelme2coco

labelme_folder = "labelme_file"
save_json_path = "coco.json"

labelme2coco.convert(labelme_folder, save_json_path)