portrule = function(host, port)
	if(port.state == "open") then
		if port.number == 443 then
			print("open-443")
		else
			print("open-80")
		end
	else
		print("closed")
	end
end

action = function (host, port)
	return nil
end