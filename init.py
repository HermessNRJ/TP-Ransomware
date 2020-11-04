import os

def main():
	#==========================================
	#Cette fonction permet de créer un répertoire
	# de test dans /tmp
    #==========================================
	os.system("mkdir /tmp/test 2>/dev/null")
	os.system("echo \"aaaaaaaa\" >/tmp/test/a.txt ")
	os.system("echo \"bbbbbbbb\" >/tmp/test/b.txt ")
	os.system("echo \"cccccccc\" >/tmp/test/c.txt ")
	#sousdossier
	os.system("mkdir /tmp/test/dossier 2>/dev/null")
	os.system("echo \"dddddddd\" >/tmp/test/dossier/d.txt ")
	os.system("echo \"eeeeeeee\" >/tmp/test/dossier/e.txt ")
	os.system("echo \"ffffffff\" >/tmp/test/dossier/f.txt ")

if __name__ == "__main__":
    main()
