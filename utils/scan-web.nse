portrule = function(host, port)
	if(port.state == "open") then

		if port.number == 80  then
			print("open-80")
		end
		if port.number == 443 then
			print("open-443")
		end
		
		print("open")
	else
		print("closed")
	end
end

action = function (host, port)
	return nil
end