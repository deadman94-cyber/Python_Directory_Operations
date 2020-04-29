import os


#uncomment which ever you want to use
#using function with os.walk

#root= print what we have specified.
#dirs= print out sub-directory from root or in root.
#files= print out all files from root and directories.

#-------------------------------------------------------------Function----------------------------------------------------------------

#def main():
#    for (root,dirs,files) in os.walk('/','topdown=true'):
#        print(root)
#        print(dirs)
#        print(files)


#print(main())

#------------------------------------------------------------without function to print directory file and sub-directory----------------------------------------------------------------

#for root,dirs,files in os.walk("/home/deadman/os/",'topdown=false'):

#    for name in dirs: (to list down sub_direcoty)
 #       print(os.path.join(root, name))
  #  for name in files:  (to list files)
   #     print(os.path.join(root,name))

#-----------------------------------------------------------without function with top-----------------------------------------------------

#for root,dirs,files in os.walk("/home/deadman/os/",'top'):
 #   for name in dirs:
  #      print(os.path.join(root, name))
   # for name in files:
    #    print(os.path.join(root, name))

#-------------------------------------------------------------------without function with followlinks--------------------------------------


#for root,dirs,files in os.walk('/home/deadman/os/','followlinks'):
 #   for name in dirs:
  #      print(os.path.join(root, name))
  #  for name in files:
   #     print(os.path.join(root, name))


