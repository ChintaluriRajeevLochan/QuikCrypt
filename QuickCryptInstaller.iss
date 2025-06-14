; QuikCrypt Installer Script

[Setup]
AppName=QuikCrypt
AppVersion=1.0
DefaultDirName={pf}\QuikCrypt
DefaultGroupName=QuikCrypt
UninstallDisplayIcon={app}\gui.exe
OutputBaseFilename=QuikCryptInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\gui.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "lock.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "encryption.key"; DestDir: "{app}"; Flags: onlyifdoesntexist

[Icons]
Name: "{group}\QuikCrypt"; Filename: "{app}\gui.exe"; IconFilename: "{app}\lock.ico"
Name: "{group}\Uninstall QuikCrypt"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\gui.exe"; Description: "Launch QuikCrypt"; Flags: nowait postinstall skipifsilent
