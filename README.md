# Diplomat
Open source repository of GPT-generated python code to test compliance controls against cloud environments.
Work in progress.

## FAQ
### Why not use a testing framework, like Inspec or pytest?
These frameworks are great for testing code against a fixture (json, yaml) that emulates the expected scenarios. This works very well for testing pre-deployment stage, as a CICD guardcrail, but with Diplomat we want to test existing deployments, at runtime.

### Why python?
We could have used the native CLI's, REST API calls or another language. The reason for python is because according to documentation, python is CodexGPT strongest language.
