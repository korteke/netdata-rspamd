# Rspamd plugin for Netdata

This [netdata](https://github.com/netdata/netdata/) plugin polls [Rspamd](https://rspamd.com/) spam filtering services API and fetch statistics.

--   
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

## Installation

* Copy **rspamd.chart.py** --> **/usr/libexec/netdata/python.d**
* Copy **rspamd.conf** --> **/etc/netdata/python.d/**
* Restart netdata service

## Usage

See beautiful charts @ Netdata UI :)

## Tested
* Ubuntu 18.04 (Bionic Beaver)
* Ubuntu 20.04 (Focal Fossa)

## Todo
* Install script