# MigAI
<div align="center">
   <img src="https://github.com/jamnicki/MigAI/assets/56606076/9cd1dbc7-b402-47a4-b4b9-f8538bd8c5a3" width="70%">
<!--   ![MigAI_logo_big](https://github.com/jamnicki/MigAI/assets/56606076/9cd1dbc7-b402-47a4-b4b9-f8538bd8c5a3) -->
</div>

## About

## Development

```
docker compose up -d
```

### Data

```
dvc remote modify --local myremote url 'azure://datacontainer'
```

```
dvc remote modify --local myremote account_name 'migaiaccname'
```

```
dvc remote modify --local myremote sas_token '<your-sas-token>'
```


Pull the latest data from the remote storage by running:
```
dvc pull
```
or
```
dvc pull <file1>.dvc <file2>.dvc
```
to pull specific files.

## 🥇 Contributors
<a  href="https://github.com/jamnicki/mig-ai/graphs/contributors">

<img  src="https://contrib.rocks/image?repo=jamnicki/mig-ai" />

</a>

## Cite

## Patrons

<div align="center">
  <img src="https://github.com/jamnicki/mig-ai/assets/56606076/1bf2f7f8-07d7-45e4-a853-00fcf2947a91" height="60">
  <img src="https://github.com/jamnicki/mig-ai/assets/56606076/514f1729-3db1-409b-a9e3-75dab11ee85f" height="60">
</div>
