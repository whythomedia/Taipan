
		if self.turn == 1:
			pname = raw_input("What is your name sailor. ")
			self.TKresponse.set("What is your name sailor. ")
			pname = self.input
			self.player_name = pname
			self.TKplayer_name.set(pname)
		self.entry.bind("<Button-1>", self.get_response(self.player_name,self.TKplayer_name))
