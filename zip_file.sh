
echo "ZIP $1 $2" 
export LEN=20

if [[ ! -z $2 ]]; then
    export LEN=$2
fi
    echo Password length $LEN

export PASS=`python random_pass.py -l $LEN`
echo "Password $PASS"
echo $PASS > $1.pass
zip -e -P $PASS $1.zip $1
echo 'DONE $1'