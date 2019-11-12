define e = Character("pp")

label start:


    scene bg room


    show pp


    e "I'm pp who is enjoying the weekend!"

    menu:
        "Enter the room":
            scene bedroom
			
	    show pp
			
	    e "Let me have a rest!"
        "Go outside":
            scene beach

	    show pp

            e ""
            
            jump start
       

    return start
