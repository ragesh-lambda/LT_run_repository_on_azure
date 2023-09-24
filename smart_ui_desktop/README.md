 <h1>Smart UI Testing With Selenium Python</h1> 
 
 <img height="400" src="https://user-images.githubusercontent.com/126776938/232534498-27618de9-6625-437e-904f-e94fc0bf38b9.png">



<p align="center">
  <a href="https://www.lambdatest.com/blog/?utm_source=github&utm_medium=repo&utm_campaign=playwright-sample" target="_bank">Blog</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/support/docs/?utm_source=github&utm_medium=repo&utm_campaign=playwright-sample" target="_bank">Docs</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/learning-hub/?utm_source=github&utm_medium=repo&utm_campaign=playwright-sample" target="_bank">Learning Hub</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/newsletter/?utm_source=github&utm_medium=repo&utm_campaign=playwright-sample" target="_bank">Newsletter</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/certifications/?utm_source=github&utm_medium=repo&utm_campaign=playwright-sample" target="_bank">Certifications</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.youtube.com/c/LambdaTest" target="_bank">YouTube</a>
</p>
&emsp;
&emsp;
&emsp;

*Learn the how to get started with Smart UI testing with Selenium Python on the LambdaTest platform.*

[<img height="58" width="200" src="https://user-images.githubusercontent.com/70570645/171866795-52c11b49-0728-4229-b073-4b704209ddde.png">](https://accounts.lambdatest.com/register?utm_source=github&utm_medium=repo&utm_campaign=playwright-sample)


## Table of Contents:

* [Pre-requisites](#pre-requisites)
* [Running Your First Selenium Python Test](#running-your-first-selenium-python-test)
* [Setting Up GitHub App Integration With SmartUI](#setting-up-github-app-integration-with-smartui)

## Pre-requisites

1. In order to run your Smart UI tests with Selenium Python, you will need to set your LambdaTest username and access key in the environment variables. Click the **Access Key** button at the top-right of the Automation Dashboard to access it.

![Screenshot 2023-04-18 132921](https://user-images.githubusercontent.com/126776938/232711334-676f1895-d223-4ee2-9bff-d82837715520.png)




**Windows**

```js
set LT_USERNAME="YOUR_USERNAME" 
set LT_ACCESS_KEY="YOUR ACCESS KEY"
```

**macOS/Linux**

```js
export LT_USERNAME="YOUR_USERNAME" 
export LT_ACCESS_KEY="YOUR ACCESS KEY"
```

2. To create a `New Project` using the SmartUI Web Application, click the **New Project** button in the top-right corner of your dashboard. 

![Screenshot 2023-04-18 133652](https://user-images.githubusercontent.com/126776938/232756183-051fc7b4-f923-410c-8168-78e44597fdc7.png)

3. Fill in the specifications such as **Platform**, **Project Name**, **Approvers**, and **Tags** as per your requirement and click **Create Project**.

![Screenshot 2023-04-18 134121](https://user-images.githubusercontent.com/126776938/232714262-56ae0be3-3ba3-4ba3-8e82-2f063657fcaf.png)

4. Install `pip` and Python.

```
sudo apt install python-pip
sudo apt install python
```

5. The recommended way to run your tests would be in `virtualenv`. It will isolate the build from other setups you may have running and ensure that the tests run with the specified versions of the modules specified in the `requirements.txt` file.

```
pip install virtualenv
```

## Running Your First Selenium Python Test

1. To get started, clone the `Python-Selenium-Sample` Repository.

```
git clone https://github.com/LambdaTest/smartui-python-sample
```

2. Next, create and activate the virtual environment in the `Python-Selenium-Sample` folder.

```
virtualenv venv
source venv/bin/activate
```
3. Inside the `Python-Selenium-Sample` folder, export the `LambdaTest Credentials`. You can get these from your automation dashboard.

4. To run your first test, run the below given command.
```
python test.py
```

## Setting Up Github App Integration with SmartUI

### Steps 1: Integrate the your Lambdatest Account with GitHub App. 

You can integrate your LambdaTest account with the GiHub application in the following ways:

- Using OAuth

![github-app-landing-92ef6e152a7302cb9ab88f5034b9ec0c](https://user-images.githubusercontent.com/126776938/232715867-f375b4df-1bc9-4e88-8340-44e986be2e9a.png)

### Step 2: Select your GitHub repository 

Go to your GitHub repository where you want to configure your SmartUI project. Check out our GitHub sample [here](https://github.com/LambdaTest/smartui-node-sample).

### Step 3: Configure your test suite

Add the `Github` capability to your current test configuration:

```bash
const capabilities: {
  platform: "Windows 10",
  browserName: "chrome",
  version: "latest",
  "smartUI.project": "Smart UI sample test",
   github: {
    "url": "https://api.github.com/repos/OWNER/REPO/statuses/commitId", // Mandatory
    "owner": "{OWNER}",  //Optional
    "repo": "{REPO}",  //Optional
    "commit": "{commitId}" //Optional
   }
}
```

### Step 4: Setting up your CI configuration

Setting up your CI workflow to execute on GitHub. Here is an example setup with `GitHub Actions`:

Go to `.github/workflows/<your_ci_file>.yml`.

```bash
    name: Execute SmartUI Test with Github App Integration
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v1

    - name: Create commit status
      run: |
        API_HOST=https://api.github.com
        # Check out the PR branch
        git checkout $GITHUB_HEAD_REF
        # Get the commit ID of the last commit
        COMMIT_ID=$(git rev-parse HEAD)
        echo "Last commit ID of PR: $COMMIT_ID"
        GITHUB_URL=$API_HOST/repos/$GITHUB_REPOSITORY/statuses/$COMMIT_ID
        echo "GITHUB_URL: $GITHUB_URL"
        echo "GITHUB_URL=$GITHUB_URL" >> $GITHUB_ENV
```

### Step5: Execute your test suite with CI

After the setup is completed, you can now execute your test suite with the Continuos Integration (CI) pipeline with any tool of your choice.

### Step 6: Commit you changes over git on a branch and raise the PR to main branch.

### Step 7: Now you will see the `lambdatest-smartui-app` in the PR.


## Documentation & Resources :books:
      
Visit the following links to learn more about LambdaTest's features, setup and tutorials around test automation, mobile app testing, responsive testing, and manual testing.

* [LambdaTest Documentation](https://www.lambdatest.com/support/docs/?utm_source=github&utm_medium=repo&utm_campaign=playwright-sample)
* [LambdaTest Blog](https://www.lambdatest.com/blog/?utm_source=github&utm_medium=repo&utm_campaign=playwright-sample)
* [LambdaTest Learning Hub](https://www.lambdatest.com/learning-hub/?utm_source=github&utm_medium=repo&utm_campaign=playwright-sample)    

## LambdaTest Community :busts_in_silhouette:

The [LambdaTest Community](https://community.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=playwright-sample) allows people to interact with tech enthusiasts. Connect, ask questions, and learn from tech-savvy people. Discuss best practises in web development, testing, and DevOps with professionals from across the globe 🌎

## What's New At LambdaTest ❓

To stay updated with the latest features and product add-ons, visit [Changelog](https://changelog.lambdatest.com/) 
      
## About LambdaTest

[LambdaTest](https://www.lambdatest.com?utm_source=github&utm_medium=repo&utm_campaign=playwright-sample) is an intelligent unified digital experience testing cloud that helps businesses drastically reduce time to market through faster test execution, ensuring quality releases and accelerated digital transformation. The platforms allows you to perform both real time and automation testing across 3000+ environments and real mobile devices, making it a top choice among other cloud testing platforms. Over 10,000+ enterprise customers and 2+ million users across 130+ countries rely on LambdaTest for their testing needs. 

### Features

* Run Selenium, Cypress, Puppeteer, Playwright, and Appium automation tests across 3000+ real desktop and mobile environments.
* Real-time cross browser testing on 3000+ environments.
* Test on Real device cloud
* Blazing fast test automation with HyperExecute
* Accelerate testing, shorten job times and get faster feedback on code changes with Test At Scale.
* Smart Visual Regression Testing on cloud
* 120+ third-party integrations with your favorite tool for CI/CD, Project Management, Codeless Automation, and more.
* Automated Screenshot testing across multiple browsers in a single click.
* Local testing of web and mobile apps.
* Online Accessibility Testing across 3000+ desktop and mobile browsers, browser versions, and operating systems.
* Geolocation testing of web and mobile apps across 53+ countries.
* LT Browser - for responsive testing across 50+ pre-installed mobile, tablets, desktop, and laptop viewports
    
[<img height="58" width="200" src="https://user-images.githubusercontent.com/70570645/171866795-52c11b49-0728-4229-b073-4b704209ddde.png">](https://accounts.lambdatest.com/register?utm_source=github&utm_medium=repo&utm_campaign=playwright-sample)
      
## We are here to help you :headphones:

* Got a query? we are available 24x7 to help. [Contact Us](mailto:support@lambdatest.com)
* For more info, visit - [LambdaTest](https://www.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=playwright-sample)
