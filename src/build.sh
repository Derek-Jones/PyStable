
# build.sh, 21 Apr 18

# gcc -Wall -fPIC -c stable_dist.c -o stable_dist.o
gcc -Wall -fPIC -c stable_pdf.c -o stable_pdf.o
gcc -Wall -fPIC -c stable_rnd.c -o stable_rnd.o
gcc -Wall -fPIC -c stable_cdf.c -o stable_cdf.o

gcc -shared -o libstable.so -lgsl *.o

