# Raspberry Pi PWM fan control
his script can control a fan connected to a Raspi's GPIO as a system service using systemd. By default it uses GPIO14 (pin 8)

## Installing
The repo is to be either cloned or symlinked at ``` /opt ``` since the service definition states that is the route to the script. So execute either of these commands:

```
sudo git clone https://github.com/msdlr/pifan.git /opt
```
```
git clone https://github.com/msdlr/pifan.git && sudo ln -s $(pwd)/pifan /opt
```
### systemd service setup
```
sudo ln -sv /opt/pifan.service /etc/systemd/system
```
### Service activation
```
sudo systemctl enable pifan.service
sudo systemctl start pifan.service
```
## Updating
After updating, you have to reload systemd services specifications, in case it changed:
```
systemctl daemon-reload
```
## Un-installing
```
sudo systemctl disable pifan.service
sudo rm -v /etc/systemd/system/pifan.service
sudo rm -rv /opt/pifan
```
