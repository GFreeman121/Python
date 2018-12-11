#!/bin/ksh
fechaProceso=$(date '+%d%m%Y')
#fechaProceso="17052018"
#fechaHoraConcatena=$(date '+%d%m%Y_%H')
rutaRaizProceso=/home/ismael/Python/CodigosPython
rutaArchivosAcciones=$rutaRaizProceso/ObtieneDataAccion/dat/$fechaProceso
archivosConcatena=$rutaArchivosAcciones/'infoAccion_'$fechaProceso
archivoBusca='infoAccion_'$fechaProceso
rutaArchivoGenera=$rutaRaizProceso/ConcatenaArchivoAccion/dat/$fechaProceso

archivoConcatenado=$rutaRaizProceso/ConcatenaArchivoAccion/dat/output/concatenado_$fechaProceso
output=$rutaRaizProceso/etl/dat/input/$fechaProceso
archivoFinal=${output}/'formato_concatena_'$fechaProceso

archivoGenera=$rutaArchivoGenera/'archivoPorHora_'$fechaProceso.info

echo "Archivo a concatenar " $archivosConcatena

if [ ! -d $rutaArchivoGenera ]; then
	mkdir $rutaArchivoGenera
fi

cd $rutaArchivosAcciones

echo "archivo a generar" $archivoGenera
for archivo in $(wc -l * | grep -v 250 | grep info | cut -c4-36)
do 
	cat $archivo >> $archivoGenera
done

awk -F"|" '{ if( $3 ~ /^+/ ) {print $0 "POSITIVA"} else if ( $3 ~ /^-/) {print $0 "NEGATIVA"} else { print $0 "NEUTRA" } }' $archivoGenera  > $archivoConcatenado

if [ ! -d ${output} ]; then

	mkdir ${output}
	
fi

sed -i 's/|-/|/g' ${archivoConcatenado}
sed -i 's/|+/|/g' ${archivoConcatenado}

cp ${archivoConcatenado} ${archivoFinal}

exit 0
