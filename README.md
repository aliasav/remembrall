# Remembrall

## Introduction

A terminal to-do list and reminder.

* Maintain a simple to-list via terminal
* Get timely terminal notifications
* Desktop notifications to also be integrated.

## Installation

Clone the project, do a:
> python setup.py install

## Usage:

* <b>Initialize remembrall:</b> <pre><code> remembrall init </pre></code>
* <b>Show items in list:</b> <pre><code> remembrall show [ids]</pre></code>
* <b>Add an item in the list:</b> <pre><code> remembrall add</pre></code>
* <b>Edits an item in the list:</b> <pre><code> remembrall edit [<id>]</pre></code>
* <b>Deletes an item from the list:</b> <pre><code> remembrall delete [<id>]</pre></code>
* <b>Purge list:</b> <pre><code> remembrall clear</pre></code>
* <pre><code> remembrall (-h | --help)</pre></code>	

### Modules:

* <b>Initializer:</b> Contains Remembrall and CronJob classes. Initializing the remembrall system on device done through here.
* <b>List:</b> Contains the todo List class, all CRUD functions of the list go here.
* <b>Constants:</b> Includes all constants used in project.
