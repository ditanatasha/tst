[CARA MENGCOMPILE FILE] -- MacOS

1. Buka file main.py pada zip yang sudah ada.
2. Pada terminal, buka terlebih dahulu directory folder dimana file yang ingin dicompile berada.
3. Run " pipenv shell " untuk membuka environment untuk mengerjakan project.
4. Kemudian, run " uvicorn main:app --reload " pada terminal untuk mendapatkan link http port nya.
5. Buka link pada browser serta tambahkan " /docs " di belakang link tersebut. 
Contoh: Link yang didapat adalah http://127.0.0.1:8000 maka pada browser 
silahkan buka link http://127.0.0.1:8000/docs
6. Akan muncul beberapa opsi untuk Get, Put, Delete dan Post. 
Klik " Try It Out " untuk mencoba masing-masing fungsi yang tersedia. 