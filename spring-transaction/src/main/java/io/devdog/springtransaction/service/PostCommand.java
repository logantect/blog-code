package io.devdog.springtransaction.service;

import io.devdog.springtransaction.domain.Post;
import lombok.Builder;
import lombok.Getter;

public class PostCommand {

  @Getter
  public static class RegisterPost {

    private String title;

    private String content;

    @Builder
    public RegisterPost(String title, String content) {
      this.title = title;
      this.content = content;
    }

    public Post toEntity() {
      return new Post(this.title, this.content);
    }
  }

  @Getter
  public static class UpdatePost {

    private String title;

    private String content;

    @Builder
    public UpdatePost(String title, String content) {
      this.title = title;
      this.content = content;
    }

  }

}
