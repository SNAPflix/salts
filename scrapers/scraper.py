"""
    SALTS XBMC Addon
    Copyright (C) 2014 tknorris

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import abc
abstractstaticmethod = abc.abstractmethod

class Scraper(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod 
    def get_name(self):
        pass

    @abc.abstractmethod 
    def resolve_link(self, link):
        return link

    @abc.abstractmethod 
    def format_source_label(self, item):
        pass

    @abc.abstractmethod 
    def get_sources(self, video_type, title, year, season='', episode=''):
        pass
