# Purpose

This is the backend for my Cloud based blog  
[Fletcher's Cloud Blog](https://cloud.fskelly.com)

## HUGO installation

I use [chocolatey](https://chocolatey.org/install) as my package manager or installation engine.

Installing HUGO is easy, I choose the extended version to allow for more capabilities.

```powershell
choco install hugo-extended -y
```


My build command

```bash
C:\ProgramData\chocolatey\lib\hugo-extended\tools\hugo.exe
```

## Create a new post

I like to create my content based upon year  
My folder structure looks like this  

```bash
content  
|---posts
    |---year
        |---postTitle
            |---index.md
```

```bash
hugo new posts/{{year}}/{{postTitle}}/index.md
```


![blog](https://img.shields.io/website-up-down-green-red/https/cloud.fskelly.com.svg)  
[![Deploy To Azure](https://github.com/fskelly/flkelly-cloudblog/actions/workflows/deploy-hugo-storage-account-copy.yml/badge.svg)](https://github.com/fskelly/flkelly-cloudblog/actions/workflows/deploy-hugo-storage-account-copy.yml)

[![Deploy To GitHub Pages](https://github.com/fskelly/cloud.fskelly.com/actions/workflows/hugo.yaml/badge.svg)](https://github.com/fskelly/flkelly-cloudblog/actions/workflows/deploy-hugo-storage-account-copy.yml)
![Website maintained](https://img.shields.io/maintenance/yes/2024?style=plastic)
