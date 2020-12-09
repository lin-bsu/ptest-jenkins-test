def set_input_port(self, port_name, conn, is_method=False):
    if port_name in self.inputPorts:
        self.inputPorts[port_name].append(conn)
    else:
        self.inputPorts[port_name] = [conn]
    if is_method:
        self.is_method[conn] = (self._latest_method_order, port_name)
        self._latest_method_order += 1