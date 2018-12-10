#!/bin/bash

process_id=ObtieneDataAccion

#Levanta entorno python
$(source /home/ismael/environments/my_env/bin/activate)
echo $HOME
if [ $? -eq 0 ]; then
	echo "entorno levantado OK"




	ejecutoPython=$(/home/ismael/environments/my_env/bin/python $HOME/Python/CodigosPython/ObtieneDataAccion/python/$process_id.py) 

fi
#$(deactivate)
