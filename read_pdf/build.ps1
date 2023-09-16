$exclude = @("venv", "read_pdf.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "read_pdf.zip" -Force