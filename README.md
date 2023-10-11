# MigAI

![MigAI_logo_big](https://github.com/jamnicki/MigAI/assets/56606076/9cd1dbc7-b402-47a4-b4b9-f8538bd8c5a3)

---

## About

## Development

```
docker compose up -d
```

### Data
On the first usage of a GDrive remote, for example when trying to dvc push tracked data for the first time, DVC will prompt you to visit a special Google authentication web page. There you'll need to sign into a Google account with the needed access to the GDrive URL in question.

Pull the latest data from the remote storage by running:
```
dvc pull
```
or
```
dvc pull <file1>.dvc <file2>.dvc
```
to pull specific files.

## Cite
