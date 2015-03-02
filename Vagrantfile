# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "mailtest"

  config.vm.network "public_network"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "deployment/all.yml"
    ansible.extra_vars = "deployment/host_vars/default"
  end

end
