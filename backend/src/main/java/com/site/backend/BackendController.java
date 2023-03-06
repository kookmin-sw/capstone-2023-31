package com.site.backend;

import java.util.Arrays;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@Controller
public class BackendController {
	
	@GetMapping("/")
	public String main() {
		return "main";
	}
	
	
	@RestController
	public class HelloController {

	    @GetMapping("/api/hello")
	    public List<String> Hello(){
	        return Arrays.asList("서버서버", "뷰뷰");
	    }
	}
}
