#include <stdio.h>
#include <string.h>
#include <errno.h>

#define PROMPT

#define GRAVITY 9.80f
#define PI 3.14159265f

void usage();

int main(int argc, char** argv) {
    if (argc < 6) {
        usage();
        return 22; // EINVAL
    }

    double mass;
    double diameter;
    double density;
    double dragCoefficient;
    double timestep;
    double area;

#ifdef PROMPT
    printf("Enter object's mass:\n");
    scanf("%lf", &mass);
    printf("Enter object's diameter:\n");
    scanf("%lf", &diamter);
    printf("Enter object's density:\n");
    scanf("%lf", &density);
    printf("Enter object's drag coefficient:\n");
    scanf("%lf", &dragCoefficient);
    printf("Enter estimation time step (ms):\n");
    scanf("%lf", &timestep);
#else
    
#endif // PROMPT

    area = PI * diameter * diameter / 4;

}
