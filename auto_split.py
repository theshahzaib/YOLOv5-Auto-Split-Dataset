import shutil,os,glob
current_dir = './dataset'

os.mkdir("train")
os.mkdir("valid")

percentage_test = 20;
counter = 1  
index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    # print('prossessing ...')
    if counter == index_test:
        counter = 1
        #file_test.write(path_data + title + '.jpg' + "\n")
        shutil.move(current_dir+"/"+title+".jpg","./valid")
        shutil.move(current_dir+"/"+title+".txt","./valid")
        #print(title)
    else:
        #file_train.write(path_data + title + '.jpg' + "\n")
        print(title+ext)
        shutil.move(current_dir+"/"+title+".jpg","./train")
        shutil.move(current_dir+"/"+title+".txt","./train")
        counter = counter + 1



current_dir_valid="./valid"


os.mkdir(current_dir_valid+"/images")
os.mkdir(current_dir_valid+"/labels")


lbl=current_dir_valid+"/labels/"
img=current_dir_valid+"/images/"

for files in glob.glob(current_dir_valid+'/*.*'):
     if files.endswith(".jpg"):
            pwd=files[:-4]+".jpg"
            print(pwd)
            shutil.move(pwd,img)
            
     elif files.endswith(".txt"):
            pwd=files[:-4]+".txt"
            print(pwd)
            shutil.move(pwd,lbl)
       

current_dir_train="./train"


os.mkdir(current_dir_train+"/images")
os.mkdir(current_dir_train+"/labels")


lbl=current_dir_train+"/labels/"
img=current_dir_train+"/images/"

for files in glob.glob(current_dir_train+'/*.*'):
     if files.endswith(".jpg"):
            pwd=files[:-4]+".jpg"
            print(pwd)
            shutil.move(pwd,img)
            
     elif files.endswith(".txt"):
            pwd=files[:-4]+".txt"
            print(pwd)
            shutil.move(pwd,lbl)
       




