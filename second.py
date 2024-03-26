

while read requirement; do
    imports+=" --hidden-import=$requirement"
done < requirements.txt

pyinstaller --onefile $imports main.py