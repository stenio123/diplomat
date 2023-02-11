# Diplomat
Open source respoitory of GPT-generated python code to test compliance controls against cloud environments.

## FAQ
### Why not use a testing framework, lyke Inspec or pytest?
These frameworks are great for testing code against a fixture (json, yaml) that emulates the expected scenarios. This is great for testing pre-deployment stage, as a CICD guardcrail, but with Diplomat we want to test existing deployments, at runtime.

### Why python?
We could have used the native CLI's, REST API calls or another language. The reason for python is because according to documentation, that is CodexGPT strongest language.