
# build.sh, 21 Apr 18

for f in *.c
   do
   gcc -Wall -fPIC -c $f -o `basename $f ".c"`.o
   done

# gcc -Wall -fPIC -c stable_pdf.c -o stable_pdf.o
# gcc -Wall -fPIC -c stable_rnd.c -o stable_rnd.o
# gcc -Wall -fPIC -c stable_cdf.c -o stable_cdf.o

gcc -shared -o libstable.so -lgsl *.o

