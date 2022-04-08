Param([parameter(mandatory=$true)][int]$int1)
$val1 = "{0:D2}" -f $int1

$data = Get-Content editorial_total.md -Encoding UTF8
$data = $data | % { $_ -replace "vol.pdf","${val1}.pdf" } | % { $_ -replace "vol","${int1}" }
$data | Out-File ./${val1}.md -Encoding UTF8

for ($i=1; $i -lt 6; $i++){
    $data = Get-Content editorial_each.md -Encoding UTF8
    $data = $data | % { $_ -replace "vol","${int1}" } | % { $_ -replace "Num","$i" }
    $data | Out-File ./${val1}-$i.md -Encoding UTF8
}