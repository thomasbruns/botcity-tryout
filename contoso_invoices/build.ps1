$exclude = @("venv", "contoso_invoices.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "contoso_invoices.zip" -Force