import sys
import yaml
import pystache
import subprocess


def main():

    with open('config.yaml','rb') as f:
        config = yaml.load(f)

    config["hostname"] = sys.argv[1]
    config["ip"] = [item["ip"] for item in config["hosts"] if item["hostname"] == config["hostname"]][0]

    renderer = pystache.Renderer()
    
    text = renderer.render_path('templates/etc/hostname', config)
    with open('/etc/hostname', 'wb') as f:
        f.write(text)

    text = renderer.render_path('templates/etc/hosts', config)
    with open('/etc/hosts', 'wb') as f:
        f.write(text)

    text = renderer.render_path('templates/etc/network/interfaces', config)
    with open('/etc/network/interfaces', 'wb') as f:
        f.write(text)

    subprocess.call(["/etc/init.d/networking", "reload"])


if __name__ == "__main__":
    main()