/**
 * Terminal Velocity Estimator.
 *
 * Authors:
 *
 * Compiled via clang term_velocity_estimator.c -lm
 */
#include <stdio.h>
#include <string.h>
#include <math.h>

#define PROMPT

#define GRAVITY 9.80f
#define PI 3.14159265f

// Conversions
#define IN_TO_M 0.0254f 

/**
 * Describes the usage of this application
 */
void usage();

/**
 * Prints out the final stats of the estimation
 */
void print_stats(
        double time,
        double termV,
        double velocity,
        double displacement,
        double drag,
        double grav);

int main(int argc, char** argv) {

    // Kinematics
    double displacement = 0;
    double velocity = 0;
    double acceleration = 0;
    double timestep = .05;
    double dt = 0;

    // Object properties
    double mass;
    double diameter;
    double density;
    double dragCoefficient;
    double area;
    
    // Forces
    double forceDrag;
    double forceGrav;
    double forceNet;

    printf("Enter object's mass (g):\n");
    scanf("%lf", &mass);
    printf("Enter object's diameter (in):\n");
    scanf("%lf", &diameter);
    printf("Enter object's density (kg/m^3):\n");
    scanf("%lf", &density);
    printf("Enter object's drag coefficient:\n");
    scanf("%lf", &dragCoefficient);
    printf("Enter estimation time step (ms):\n");
    scanf("%lf", &timestep);

    // Convert units and calculate
    mass /= 1000; // g to kg
    diameter *= IN_TO_M; // in to m

    area = PI * diameter * diameter / 4;
    forceGrav = mass * GRAVITY;

    // Calculate TV 100%
    double tv = sqrt((2 * forceGrav) / (density * area * dragCoefficient));

    // Loop until 90% of terminal velocity
    while (velocity < tv * .9) {
        forceDrag = .5 * density * area * dragCoefficient * velocity * velocity;
        forceNet = forceGrav - forceDrag;
        acceleration = forceNet / mass;
        displacement += velocity * timestep;
        velocity += acceleration * timestep;
        dt += timestep;
    }

    print_stats(dt, tv, velocity, displacement, forceDrag, forceGrav);
}

void usage() {
    printf("Terminal Velocity Script - calculate stats at 90%% terminal velocity.\n");
    printf("No command line usage\n");
}

void print_stats(
        double time,
        double termV,
        double velocity, 
        double displacement,
        double drag,
        double grav) {
    printf("--90%% Terminal Velocity----------------------------------\n");
    printf("Calculated Terminal V: %g  90%%: %g\n", termV, termV * .9);
    printf("Estimated 90%% Terminal V: %g  Error: %g%%\n",
            velocity, fabs(termV * .9 - velocity) / (termV * .9) * 100);
    printf("Force of Drag: %g  Force of Gravity: %g\n", drag, grav);
    printf("-Time: %g s Distance: %g m\n", time, displacement);
    printf("---------------------------------------------------------\n");
}

