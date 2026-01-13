# Lesson 04: Jenkins Architecture And Automation

### Shorthand Notes

### Jenkins Home Structure

Clearly understand what the Jenkins home directory stores: configurations, logs, and plugins.

### Distributed Architecture

The Jenkins controller acts as the significant brain, while agent nodes perform like motivated hands, managing the build process.

### Parameterized Build

If someone asks what a dynamic build is, we can confidently answer that branch names, version numbers, and other parameters can be flexibly customized before each build begins.

### Poll SCM

LOL, it's like a GitHub detective, regularly eager to spy on new changes right on time.

### Environment Variables

These are dynamic values that automatically change with every single build.

### Workspace

This is where code is pulled from GitHub, plugins are installed, and logs are executed—all within this temporary working area.

### Execute Shell

You can test build steps using pre-customized shell scripts.
