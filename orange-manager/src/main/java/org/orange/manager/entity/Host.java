package org.orange.manager.entity;

import org.orange.manager.entity.dto.HostDto;

/**
 * @author hiram 2019年12月23日 22:22
 */
public class Host {
    private Long id;
    private String ip;
    private String hostname;
    private String name;
    private String desc;
    private int status;

    public Host() {
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getIp() {
        return ip;
    }

    public void setIp(String ip) {
        this.ip = ip;
    }

    public String getHostname() {
        return hostname;
    }

    public void setHostname(String hostname) {
        this.hostname = hostname;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public static Host fromDto(HostDto hostDto) {
        Host host = new Host();
        host.setId(hostDto.getId());
        host.setIp(hostDto.getIp());
        host.setHostname(hostDto.getHostname());
        host.setName(hostDto.getName());
        host.setDesc(hostDto.getDesc());
        return host;
    }

    @Override
    public String toString() {
        return "Host{" +
                "id=" + id +
                ", ip='" + ip + '\'' +
                ", hostname='" + hostname + '\'' +
                ", name='" + name + '\'' +
                ", desc='" + desc + '\'' +
                ", status=" + status +
                '}';
    }
}
